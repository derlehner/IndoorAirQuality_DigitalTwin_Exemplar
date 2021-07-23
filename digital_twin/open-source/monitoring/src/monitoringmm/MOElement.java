/**
 */
package monitoringmm;

import org.eclipse.emf.common.util.EList;

/**
 * <!-- begin-user-doc -->
 * A representation of the model object '<em><b>MO Element</b></em>'.
 * <!-- end-user-doc -->
 *
 * <p>
 * The following features are supported:
 * </p>
 * <ul>
 *   <li>{@link monitoringmm.MOElement#getProperties <em>Properties</em>}</li>
 * </ul>
 *
 * @see monitoringmm.MonitoringmmPackage#getMOElement()
 * @model abstract="true"
 * @generated
 */
public interface MOElement extends MonitorableElement {
	/**
	 * Returns the value of the '<em><b>Properties</b></em>' containment reference list.
	 * The list contents are of type {@link monitoringmm.MOElement}.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @return the value of the '<em>Properties</em>' containment reference list.
	 * @see monitoringmm.MonitoringmmPackage#getMOElement_Properties()
	 * @model containment="true"
	 * @generated
	 */
	EList<MOElement> getProperties();

} // MOElement
