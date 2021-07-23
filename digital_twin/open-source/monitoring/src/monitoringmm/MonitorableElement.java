/**
 */
package monitoringmm;


/**
 * <!-- begin-user-doc -->
 * A representation of the model object '<em><b>Monitorable Element</b></em>'.
 * <!-- end-user-doc -->
 *
 * <p>
 * The following features are supported:
 * </p>
 * <ul>
 *   <li>{@link monitoringmm.MonitorableElement#getTopic <em>Topic</em>}</li>
 *   <li>{@link monitoringmm.MonitorableElement#isSync <em>Sync</em>}</li>
 * </ul>
 *
 * @see monitoringmm.MonitoringmmPackage#getMonitorableElement()
 * @model abstract="true"
 * @generated
 */
public interface MonitorableElement extends NamedElement {
	/**
	 * Returns the value of the '<em><b>Topic</b></em>' attribute.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @return the value of the '<em>Topic</em>' attribute.
	 * @see #setTopic(String)
	 * @see monitoringmm.MonitoringmmPackage#getMonitorableElement_Topic()
	 * @model
	 * @generated
	 */
	String getTopic();

	/**
	 * Sets the value of the '{@link monitoringmm.MonitorableElement#getTopic <em>Topic</em>}' attribute.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @param value the new value of the '<em>Topic</em>' attribute.
	 * @see #getTopic()
	 * @generated
	 */
	void setTopic(String value);

	/**
	 * Returns the value of the '<em><b>Sync</b></em>' attribute.
	 * The default value is <code>"false"</code>.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @return the value of the '<em>Sync</em>' attribute.
	 * @see #setSync(boolean)
	 * @see monitoringmm.MonitoringmmPackage#getMonitorableElement_Sync()
	 * @model default="false"
	 * @generated
	 */
	boolean isSync();

	/**
	 * Sets the value of the '{@link monitoringmm.MonitorableElement#isSync <em>Sync</em>}' attribute.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @param value the new value of the '<em>Sync</em>' attribute.
	 * @see #isSync()
	 * @generated
	 */
	void setSync(boolean value);

} // MonitorableElement
